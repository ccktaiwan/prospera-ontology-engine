import pytest, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from monitoring_hook import trigger_monitoring, auto_remediate

_LOG = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "execution_log.jsonl")

def test_trigger_monitoring():
    trigger_monitoring({"test": True})
    assert os.path.exists(_LOG)

def test_auto_remediate():
    r = auto_remediate({"error": "test"})
    assert r["status"] == "ATTEMPTED"
