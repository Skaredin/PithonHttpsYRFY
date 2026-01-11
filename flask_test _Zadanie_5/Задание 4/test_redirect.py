import io
import pytest
from redirect import Redirect

def test_redirect_both():
    out = io.StringIO()
    err = io.StringIO()

    try:
        with Redirect(stdout=out, stderr=err):
            print("Hello stdout")
            raise Exception("Hello stderr")
    except Exception:
        pass

    assert "Hello stdout" in out.getvalue()
    assert "Hello stderr" in err.getvalue()


def test_redirect_only_stdout():
    out = io.StringIO()

    with Redirect(stdout=out):
        print("Only stdout")

    assert "Only stdout" in out.getvalue()


def test_redirect_only_stderr():
    err = io.StringIO()

    try:
        with Redirect(stderr=err):
            raise Exception("Only stderr")
    except Exception:
        pass

    assert "Only stderr" in err.getvalue()


def test_restore_original():
    import sys
    old_stdout = sys.stdout
    old_stderr = sys.stderr

    out = io.StringIO()
    err = io.StringIO()

    try:
        with Redirect(stdout=out, stderr=err):
            pass
    except Exception:
        pass

    # Потоки восстановлены
    assert sys.stdout == old_stdout
    assert sys.stderr == old_stderr
