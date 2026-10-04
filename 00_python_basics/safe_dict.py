"""
PROBLEM:
Safely extract values from a messy dictionary with fallback defaults
to prevent KeyError exceptions.

Example:
    Input:  {"id": 101, "username": "alice"}
    Output: {"id": 101, "username": "alice", "role": "member", "points": 0}
"""

def sanitize_user_profile(user_dict: dict) -> dict:
    return {
        "id": user_dict["id"],
        "username": user_dict["username"],
        "role": user_dict.get("role", "member"),
        "points": user_dict.get("points", 0)
    }

if __name__ == "__main__":
    raw_user = {"id": 101, "username": "alice"}
    print(sanitize_user_profile(raw_user))