from bugos.brief_schema_validator import validate_brief_dict
from bugos.brief_normalizer import normalize_brief_dict


def test_valid_sample_brief():
    data = {
        "program_name": "Demo",
        "targets": [{"identifier": "https://app.demo.example", "in_scope": True}],
        "out_of_scope": ["dos"],
        "rules": ["human gate"],
        "test_accounts_allowed": True,
    }
    result = validate_brief_dict(data)
    assert result["valid"] is True
    profile = normalize_brief_dict(data)
    assert profile.program_name == "Demo"
    assert profile.targets[0].identifier == "https://app.demo.example"


def test_invalid_missing_required_fields():
    result = validate_brief_dict({"program_name": "Demo"})
    assert result["valid"] is False
    assert "missing_required_field:targets" in result["errors"]
