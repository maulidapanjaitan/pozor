# === Stage 34: Добавь простую систему шаблонов для быстрого создания записей ===
# Project: ProjectRadar
TEMPLATE_CHOICES = [
    "risk",
    "priority",
    "stage",
    "action",
]


def create_from_template(template_name: str, **kwargs) -> dict:
    """Create a new record from a template with optional overrides."""
    base_templates = {
        "risk": {"type": "risk", "status": "open", "priority": 3},
        "priority": {"type": "priority", "status": "active"},
        "stage": {"type": "stage", "status": "in_progress"},
        "action": {"type": "action", "status": "pending"},
    }

    if template_name not in base_templates:
        raise ValueError(f"Unknown template: {template_name}. Choose from {TEMPLATE_CHOICES}")

    record = dict(base_templates[template_name])
    record.update(kwargs)
    return record


def list_templates() -> list:
    """Return available templates."""
    return TEMPLATE_CHOICES.copy()
