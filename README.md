# Automated semantic releases

Testing automation of GitHub and PyPI releases with
[`python-semantic-release`](pkg-py-sem-rel). See
[documentation][docs-py-sem-rel]. Configuration in
[`setup.cfg`](setup.cfg).

## Commands

Dry run with verbose output:

```bash
semantic-release publish --noop -v DEBUG
```

Print changelog without changing it:

```bash
semantic-release changelog --noop
```

Publish release as configured:

```bash
semantic-release publish
```

## To do

- [x] Configure locally, with `--noop` option
  - Create [`setup.cfg`](setup.cfg) file ([available options][conf-py-sem-rel])
- [x] Configure GitHub release on
  <https://github.com/uniqueg/semantic-release>
  - Create GitHub API token (scope `public_repo`)
  - Export `GH_TOKEN` environment variable
- [x] Configure PyPI release on <https://test.pypi.org/>
  - Create PyPI token (scope to individual project, if possible)
  - Export `PYPI_TOKEN` environment variable
- [] Configure Travis CI integration
  - Set environment variables `GH_TOKEN` and `PYPI_TOKEN` in Travis CI
  - Add commands to configure, install and run `semantic-release` in
    Travis CI:

  ```yaml
  after_success:
  - git config --global user.name "semantic-release (via TravisCI)"
  - git config --global user.email "semantic-release@travis"
  - pip install python-semantic-release
  - semantic-release publish
  ```

- [] Configure development (`dev`) branch and release only when merging into
  release branch (`main`)

[pkg-py-sem-rel]: <https://github.com/relekang/python-semantic-release>
[conf-py-sem-rel]: <https://python-semantic-release.readthedocs.io/en/latest/configuration.html>
[docs-py-sem-rel]: <http://python-semantic-release.readthedocs.io/>
