import compileall

def test_compilation():
    compileall.compile_dir('.', force=True)
