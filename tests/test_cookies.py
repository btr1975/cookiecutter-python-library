def test_bake_project_no_cli(cookies, bake_project_no_cli_data):
    result = cookies.bake(extra_context=bake_project_no_cli_data)

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project.basename == 'python-no-cli'
    assert result.project.isdir()
    assert result.project.join('README.md').isfile()
    assert result.project.join('python_no_cli').isdir()
    assert not result.project.join('python_no_cli', 'python_no_cli_cli.py').isfile()
    assert not result.project.join('python_no_cli', 'example.py').isfile()


def test_bake_project_cli(cookies, bake_project_cli_data):
    result = cookies.bake(extra_context=bake_project_cli_data)

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project.basename == 'python-with-cli'
    assert result.project.isdir()
    assert result.project.join('README.md').isfile()
    assert result.project.join('python_with_cli').isdir()
    assert result.project.join('python_with_cli', 'python_with_cli_cli.py').isfile()
    assert result.project.join('python_with_cli', 'example.py').isfile()
