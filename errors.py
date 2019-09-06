class HockeyError(Exception):
    pass


class UserHasVotedError(HockeyError):
    pass


class VotingHasEndedError(HockeyError):
    pass


class NotAValidTeamError(HockeyError):
    pass


class InvalidFileError(HockeyError):
    pass
