# Tag-based package and image versioning plan

## Desired behavior

| Git event | Python package version | GHCR image tag | Publish? |
| --- | --- | --- | --- |
| Push to `main` | `0.0.0.dev<GITHUB_RUN_NUMBER>` | `dev` | Yes |
| Push of release tag `X.Y.Z` | Exactly `X.Y.Z` | Exactly `X.Y.Z` | Yes |
| Pull request to `main` | Development version for that run | Temporary build tag | No |

Release tags use three numeric components without a `v` prefix (for example, `1.2.3`). This makes the Git tag, Python distribution version, and Docker image tag identical. Reject any tag that does not match `^[0-9]+\.[0-9]+\.[0-9]+$` before building or publishing. `dev` is a mutable image tag; the development package version is unique per run because `dev` alone is not a valid Python package version.

## Changes to make

1. **Derive package versions from Git.** In `pyproject.toml`, replace the fixed `project.version = "0.1.0"` with `project.dynamic = ["version"]`, add `hatch-vcs` to `build-system.requires`, and configure `[tool.hatch.version] source = "vcs"`. Regenerate `uv.lock`. Replace the stale hard-coded `ocpp_mqtt_bridge/__version__.py` value (`0.0.0`) with a generated version file or a read of installed distribution metadata, so code and package metadata agree.
2. **Resolve one version per workflow run.** Extend `.github/workflows/docker-image.yml` to trigger on pushes to `main`, pushes of release tags, and pull requests. Add a version step or job that validates a tag and exports `PACKAGE_VERSION` and `IMAGE_TAG`. Use `0.0.0.dev${GITHUB_RUN_NUMBER}` and `dev` for `main`; use the exact numeric tag for releases. Check out full Git history and tags (`fetch-depth: 0`) for VCS versioning.
3. **Use the resolved version in both builds.** Set `SETUPTOOLS_SCM_PRETEND_VERSION` to `PACKAGE_VERSION` for the uv build/test steps and pass `PACKAGE_VERSION` as a Docker build argument. In the Docker build stage, expose that value to hatch-vcs while `uv pip install /src` builds the package. This avoids relying on `.git` being present in the Docker build context. Add an OCI version label and assert that `importlib.metadata.version("ocpp-mqtt-bridge")` equals the build argument.
4. **Publish only the requested image tag.** Configure `docker/build-push-action` to publish `ghcr.io/intrinseca/ocpp-mqtt-bridge:dev` from `main` and `ghcr.io/intrinseca/ocpp-mqtt-bridge:X.Y.Z` from a release tag. Pull requests build without pushing. Avoid the current extra branch, PR, SHA, major, and minor aliases unless a separate requirement calls for them. Make the Docker job depend on both tests and pre-commit linting.
5. **Document releases.** Add a short README section: merge the release commit to `main`, create and push an annotated `X.Y.Z` tag at that commit, then verify that the published image tag and installed package version both equal `X.Y.Z`. The repository currently has no tags, so the first release tag must be created after the workflow change lands.

## Verification before publishing

- Run `uv lock --check`, tests, mypy, and pre-commit with Python 3.12.
- Build a wheel with a simulated development version and inspect its metadata; build another with a simulated release version and confirm the wheel filename and metadata use that exact version.
- Build the Docker image locally for both versions and inspect its installed package version and OCI version label.
- Confirm CI publishes `dev` only on a `main` push, the exact numeric tag only on a release-tag push, and nothing on a pull request. Confirm malformed tags fail before the publish step.
- Check that the existing Docker dependency installation (`uv sync --frozen --no-install-project`) still works with a dynamic project version; adjust the lock or install flow if it does not.

The logging changes already in this clone are uncommitted. Keep them intact while implementing this plan. No Flux manifests or cluster state need changing for the versioning work; the Flux deployment currently uses a pinned image digest.
