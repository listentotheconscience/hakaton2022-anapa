class ResolveOutput:
    @classmethod
    def get_status(cls, line):
        is_unloaded = cls._is_unloaded(line)
        is_near_can_or_in_can = cls._is_near_can_or_in_can(line)
        if is_near_can_or_in_can is True and is_unloaded is True:
            return 'unloaded'
        elif is_unloaded is True:
            return 'unloaded'
        elif is_near_can_or_in_can is True:
            return 'is_near_can_or_in_can'
        else:
            return None

    @classmethod
    def get_type(cls, status):
        if 'unloaded' in status:
            return 'inactive'
        else:
            return 'active'

    @classmethod
    def resolve_status(cls, unloaded, near):
        if unloaded is 0 and near is 0:
            return None
        return 'unloaded' if unloaded < near else 'is_near_can_or_in_can'


    @classmethod
    def _is_unloaded(cls, line):
        if 'person' in line and 'vest' in line:
            return True
        if 'truck' in line:
            return True
        return False

    @classmethod
    def _is_near_can_or_in_can(cls, line):
        if 'can' in line or 'garbage' in line or 'bigbag' in line:
            return True
        return False
