def test_bake_project_no_cli(cookies, bake_project_no_cli_data):
    result = cookies.bake(extra_context=bake_project_no_cli_data)

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_path.name == 'python-no-cli'
    assert result.project_path.is_dir()
    assert result.project_path.joinpath('README.md').is_file()
    assert result.project_path.joinpath('python_no_cli').is_dir()
    assert not result.project_path.joinpath('python_no_cli', 'python_no_cli_cli.py').is_file()
    assert not result.project_path.joinpath('python_no_cli', 'example.py').is_file()


def test_bake_project_cli(cookies, bake_project_cli_data):
    result = cookies.bake(extra_context=bake_project_cli_data)

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_path.name == 'python-with-cli'
    assert result.project_path.is_dir()
    assert result.project_path.joinpath('README.md').is_file()
    assert result.project_path.joinpath('python_with_cli').is_dir()
    assert result.project_path.joinpath('python_with_cli', 'python_with_cli_cli.py').is_file()
    assert result.project_path.joinpath('python_with_cli', 'example.py').is_file()
