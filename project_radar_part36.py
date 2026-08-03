# === Stage 36: Добавь проверку целостности данных и функцию ремонта простых проблем ===
# Project: ProjectRadar
def check_and_repair(self, report):
        issues = []
        if not isinstance(report, dict):
            return False, ["report is not a dict"]
        for k in ("name", "risk_level", "priority", "status"):
            if k not in report:
                missing = [k] + ([missing] if 'missing' in issues else [])
                issues.append(f"missing field: {k}")
        risk_map = {"low": 0, "medium": 1, "high": 2}
        for key in ("risk_level", "priority"):
            val = report.get(key)
            if isinstance(val, str):
                try:
                    report[key] = int(val.replace(" ", ""))
                except ValueError:
                    issues.append(f"{key} cannot be converted to int")

        status_map = {"active": 1, "planned": 2, "completed": 3, "cancelled": 4}
        for key in ("status",):
            val = report.get(key)
            if isinstance(val, str) and val.lower() in status_map:
                report[key] = int(status_map[val.lower()])

        if issues:
            return False, issues
        return True, ["OK"]
