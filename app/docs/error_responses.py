examples = {
    "start before end": {
        "value": {
            "code": "INVALID_ARGUMENT",
            "message": "start time must be before end time.",
        }
    },
    "time unit": {
        "value": {
            "code": "INVALID_ARGUMENT",
            "message": "Time must be set at the beginning of an hour (e.g., 12:00:00).",
        }
    },
    "3days after": {
        "value": {
            "code": "INVALID_ARGUMENT",
            "message": "schedule can only be made up to 3days before the exam start",
        }
    },
    "limit over": {
        "value": {
            "code": "INVALID_ARGUMENT",
            "message": "Applicants must be less than or equal to the limit. limit(...) < applicants(...). range(start~end)",
        }
    },
    "canceled info fix": {
        "value": {
            "code": "INVALID_STATE",
            "message": "Can't update schedule while in CANCELED status.",
        }
    },
    "not exist resource": {
        "value": {
            "code": "NOT_EXIST_RESOURCE",
            "message": "schedule is not exists. schedule_id: 'schedule_id'",
        }
    },
    "not owner resource": {
        "value": {
            "code": "ACCESS_DENIED",
            "message": "schedule changes only owner. your are not this schedule owner. schedule_id: '...'",
        }
    },
    "must canceled": {
        "value": {
            "code": "INVALID_ARGUMENT",
            "message": "change status must be CANCELED.",
        }
    },
    "cant be canceled": {
        "value": {
            "code": "INVALID_STATE",
            "message": "schedule can't change status '...' to 'CANCEL'",
        }
    },
    "cant same": {
        "value": {
            "code": "INVALID_ARGUMENT",
            "message": "as_is and to_be are the same. can't change to same status. status(...)",
        }
    },
    "search range over": {
        "value": {
            "code": "INVALID_ARGUMENT",
            "message": "The search period cannot exceed 14 days.",
        }
    },
}

admin_change_schedule = {
    400: {
        "description": "invalid request error",
        "content": {
            "application/json": {
                "examples": {
                    "start before end": examples["start before end"],
                    "time unit": examples["time unit"],
                    "3days after": examples["3days after"],
                    "limit over": examples["limit over"],
                    "canceled info fix": examples["canceled info fix"],
                }
            }
        },
    },
    404: {
        "description": "not exist resource",
        "content": {
            "application/json": {"example": examples["not exist resource"]["value"]}
        },
    },
}

admin_change_schedule_status = {
    400: {
        "description": "invalid request error",
        "content": {
            "application/json": {
                "examples": {
                    "start before end": examples["start before end"],
                    "time unit": examples["time unit"],
                    "3days after": examples["3days after"],
                    "limit over": examples["limit over"],
                    "canceled info fix": examples["canceled info fix"],
                }
            }
        },
    },
    404: {
        "description": "not exist resource",
        "content": {
            "application/json": {"example": examples["not exist resource"]["value"]}
        },
    },
}

customer_create_schedule = {
    400: {
        "description": "invalid request error",
        "content": {
            "application/json": {
                "examples": {
                    "start before end": examples["start before end"],
                    "time unit": examples["time unit"],
                    "3days after": examples["3days after"],
                    "limit over": examples["limit over"],
                }
            }
        },
    },
    404: {
        "description": "not exist resource",
        "content": {
            "application/json": {"example": examples["not exist resource"]["value"]}
        },
    },
}

customer_change_schedule = {
    400: {
        "description": "invalid request error",
        "content": {
            "application/json": {
                "examples": {
                    "start before end": examples["start before end"],
                    "time unit": examples["time unit"],
                    "3days after": examples["3days after"],
                    "limit over": examples["limit over"],
                    "canceled info fix": examples["canceled info fix"],
                }
            }
        },
    },
    403: {
        "description": "not owner resource",
        "content": {
            "application/json": {"example": examples["not owner resource"]["value"]}
        },
    },
    404: {
        "description": "not exist resource",
        "content": {
            "application/json": {"example": examples["not exist resource"]["value"]}
        },
    },
}

customer_change_schedule_status = {
    400: {
        "description": "invalid request error",
        "content": {
            "application/json": {
                "examples": {
                    "start before end": examples["start before end"],
                    "time unit": examples["time unit"],
                    "3days after": examples["3days after"],
                    "limit over": examples["limit over"],
                    "must canceled": examples["must canceled"],
                    "cant be canceled": examples["cant be canceled"],
                    "cant same": examples["cant same"],
                }
            }
        },
    },
    403: {
        "description": "not owner resource",
        "content": {
            "application/json": {"example": examples["not owner resource"]["value"]}
        },
    },
    404: {
        "description": "not exist resource",
        "content": {
            "application/json": {"example": examples["not exist resource"]["value"]}
        },
    },
}

get_schedule_slots = {
    400: {
        "description": "invalid request error",
        "content": {
            "application/json": {
                "examples": {
                    "3days after": examples["3days after"],
                    "start before end": examples["start before end"],
                    "search range over": examples["search range over"],
                }
            }
        },
    },
}
