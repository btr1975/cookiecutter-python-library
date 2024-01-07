def test_bake_project_no_cli_podman(cookies, bake_project_no_cli_podman_data):
    result = cookies.bake(extra_context=bake_project_no_cli_podman_data)

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_path.name == 'python-no-cli'
    assert result.project_path.is_dir()
    assert result.project_path.joinpath('README.md').is_file()
    assert result.project_path.joinpath('python_no_cli').is_dir()
    assert not result.project_path.joinpath('python_no_cli', 'python_no_cli_cli.py').is_file()
    assert not result.project_path.joinpath('python_no_cli', 'example.py').is_file()
    assert result.project_path.joinpath('containers', 'Containerfile').is_file()
    assert not result.project_path.joinpath('containers', 'Dockerfile').is_file()


def test_bake_project_no_cli_docker(cookies, bake_project_no_cli_docker_data):
    result = cookies.bake(extra_context=bake_project_no_cli_docker_data)

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_path.name == 'python-no-cli'
    assert result.project_path.is_dir()
    assert result.project_path.joinpath('README.md').is_file()
    assert result.project_path.joinpath('python_no_cli').is_dir()
    assert not result.project_path.joinpath('python_no_cli', 'python_no_cli_cli.py').is_file()
    assert not result.project_path.joinpath('python_no_cli', 'example.py').is_file()
    assert not result.project_path.joinpath('containers', 'Containerfile').is_file()
    assert result.project_path.joinpath('containers', 'Dockerfile').is_file()


def test_bake_project_cli_podman(cookies, bake_project_cli_podman_data):
    result = cookies.bake(extra_context=bake_project_cli_podman_data)

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_path.name == 'python-with-cli'
    assert result.project_path.is_dir()
    assert result.project_path.joinpath('README.md').is_file()
    assert result.project_path.joinpath('python_with_cli').is_dir()
    assert result.project_path.joinpath('python_with_cli', 'python_with_cli_cli.py').is_file()
    assert result.project_path.joinpath('python_with_cli', 'example.py').is_file()
    assert result.project_path.joinpath('containers', 'Containerfile').is_file()
    assert not result.project_path.joinpath('containers', 'Dockerfile').is_file()


def test_bake_project_cli_docker(cookies, bake_project_cli_docker_data):
    result = cookies.bake(extra_context=bake_project_cli_docker_data)

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_path.name == 'python-with-cli'
    assert result.project_path.is_dir()
    assert result.project_path.joinpath('README.md').is_file()
    assert result.project_path.joinpath('python_with_cli').is_dir()
    assert result.project_path.joinpath('python_with_cli', 'python_with_cli_cli.py').is_file()
    assert result.project_path.joinpath('python_with_cli', 'example.py').is_file()
    assert not result.project_path.joinpath('containers', 'Containerfile').is_file()
    assert result.project_path.joinpath('containers', 'Dockerfile').is_file()
