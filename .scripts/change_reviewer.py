import json


def load_json(file_path):
    info = None
    with open(file_path, "r") as f:
        info = json.load(f)
    print("Load and parse reviewer_info.json")
    return info


def change_reviewer(info):
    pointer = info["pointer"]  # 시작 포인터
    total = info["total"]  # 총 명수
    rotation = info["rotation"]  # 로테이션 명수
    members = info["members"]  # 팀원 리스트

    pointer = (pointer + rotation) % total  # 포인터 변경
    info["pointer"] = pointer
    info["reviewers"] = [members[i%total] for i in range(pointer, pointer+rotation)]
    print("This week reviewer:", *info["reviewers"])
    return info


def save_json(file_path, info):
    with open(file_path, "w") as f:
        json.dump(info, f)
    print("Save changed info in reviewer_info.json")


file_path = "./.scripts/reviewer_info.json"
info = load_json(file_path)
info = change_reviewer(info)
save_json(file_path, info)
