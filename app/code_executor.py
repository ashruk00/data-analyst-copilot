def run_code(code, df):
    local_vars = {"df": df.copy()}
    try:
        exec(code, {}, local_vars)
        result = local_vars.get("result", None)
        return result, None
    except Exception as e:
        return None, str(e)

