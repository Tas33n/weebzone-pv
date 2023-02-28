from bot import CMD_SUFFIX
import os
def getCommand(name: str, command: str):
    try:
        if len(os.environ[name]) == 0:
            raise KeyError
        return os.environ[name]
    except KeyError:
        return command


class _BotCommands:
    def __init__(self):
        self.StartCommand = getCommand(f'START_COMMAND', f'start{CMD_SUFFIX}')
        self.MirrorCommand = getCommand('MIRROR_COMMAND', f'mirror{CMD_SUFFIX}')
        self.UnzipMirrorCommand = getCommand('UNZIP_COMMAND', f'unzipmirror{CMD_SUFFIX}')
        self.ZipMirrorCommand = getCommand('ZIP_COMMAND', f'zipmirror{CMD_SUFFIX}')
        self.CancelMirror = getCommand('CANCEL_COMMAND', f'cancel{CMD_SUFFIX}')
        self.CancelAllCommand = getCommand('CANCEL_ALL_COMMAND', f'cancelall{CMD_SUFFIX}')
        self.ListCommand = getCommand('LIST_COMMAND', f'list{CMD_SUFFIX}')
        self.SearchCommand = getCommand('SEARCH_COMMAND', f'search{CMD_SUFFIX}')
        self.StatusCommand = getCommand('STATUS_COMMAND', f'status{CMD_SUFFIX}')
        self.AuthorizedUsersCommand = getCommand('USERS_COMMAND', f'users{CMD_SUFFIX}')
        self.PaidUsersCommand = getCommand('PAID_COMMAND', f'paid{CMD_SUFFIX}')
        self.AddPaidCommand = getCommand('ADDPAID_COMMAND', f'addpaid{CMD_SUFFIX}')
        self.RmPaidCommand = getCommand('RMPAID_COMMAND', f'rmpaid{CMD_SUFFIX}')
        self.PreNameCommand = getCommand('PRENAME_COMMAND', f'prename{CMD_SUFFIX}')
        self.SufNameCommand = getCommand('SUFFIX_COMMAND', f'suffix{CMD_SUFFIX}')
        self.CaptionCommand = getCommand('CAPTION_COMMAND', f'caption{CMD_SUFFIX}')
        self.UserLogCommand = getCommand('DUMPID_COMMAND', f'dumpid{CMD_SUFFIX}')
        self.RemnameCommand = getCommand('REMNAME_COMMAND', f'remname{CMD_SUFFIX}')
        self.AuthorizeCommand = getCommand('AUTH_COMMAND', f'authorize{CMD_SUFFIX}')
        self.UnAuthorizeCommand = getCommand('UNAUTH_COMMAND', f'unauthorize{CMD_SUFFIX}')
        self.AddSudoCommand = getCommand('ADDSUDO_COMMAND', f'addsudo{CMD_SUFFIX}')
        self.RmSudoCommand = getCommand('RMSUDO_COMMAND', f'rmsudo{CMD_SUFFIX}')
        self.PingCommand = getCommand('PING_COMMAND', f'ping{CMD_SUFFIX}')
        self.RestartCommand =  getCommand('RESTART_COMMAND', f'restart{CMD_SUFFIX}')
        self.StatsCommand = getCommand('STATS_COMMAND', f'stats{CMD_SUFFIX}')
        self.HelpCommand = getCommand('HELP_COMMAND', f'help{CMD_SUFFIX}')
        self.LogCommand = getCommand('LOG_COMMAND', f'log{CMD_SUFFIX}')
        self.BtSelectCommand = getCommand('BTSEL_COMMAND', f'btsel{CMD_SUFFIX}')
        self.SpeedCommand = getCommand('SPEEDTEST_COMMAND', f'speedtest{CMD_SUFFIX}')
        self.CloneCommand = getCommand('CLONE_COMMAND', f'clone{CMD_SUFFIX}')
        self.CountCommand = getCommand('COUNT_COMMAND', f'count{CMD_SUFFIX}')
        self.WatchCommand =  getCommand('WATCH_COMMAND', f'watch{CMD_SUFFIX}')
        self.ZipWatchCommand = getCommand('ZIPWATCH_COMMAND', f'zipwatch{CMD_SUFFIX}')
        self.ScrapeCommand = getCommand('SCRAPE_COMMAND', f'scrape{CMD_SUFFIX}')
        self.QbMirrorCommand = getCommand('QBMIRROR_COMMAND', f'qbmirror{CMD_SUFFIX}')
        self.QbUnzipMirrorCommand = getCommand('QBUNZIP_COMMAND', f'qbunzipmirror{CMD_SUFFIX}')
        self.QbZipMirrorCommand = getCommand('QBZIP_COMMAND', f'qbzipmirror{CMD_SUFFIX}')
        self.DeleteCommand = getCommand('DELETE_COMMAND', f'del{CMD_SUFFIX}')
        self.ShellCommand = getCommand('SHELL_COMMAND', f'shell{CMD_SUFFIX}')
        self.ExecHelpCommand = getCommand('EXEHELP_COMMAND', f'exechelp{CMD_SUFFIX}')
        self.LeechSetCommand = getCommand('LEECHSET_COMMAND', f'leechset{CMD_SUFFIX}')
        self.SetThumbCommand = getCommand('SETTHUMB_COMMAND', f'setthumb{CMD_SUFFIX}')
        self.LeechCommand = getCommand('LEECH_COMMAND', f'leech{CMD_SUFFIX}')
        self.UnzipLeechCommand = getCommand('UNZIPLEECH_COMMAND', f'unzipleech{CMD_SUFFIX}')
        self.ZipLeechCommand = getCommand('ZIPLEECH_COMMAND', f'zipleech{CMD_SUFFIX}')
        self.QbLeechCommand = getCommand('QBLEECH_COMMAND', f'qbleech{CMD_SUFFIX}')
        self.QbUnzipLeechCommand = getCommand('QBZIPLEECH_COMMAND', f'qbunzipleech{CMD_SUFFIX}')
        self.QbZipLeechCommand = getCommand('QBUNZIPLEECH_COMMAND', f'qbzipleech{CMD_SUFFIX}')
        self.LeechWatchCommand = getCommand('LEECHWATCH_COMMAND',  f'leechwatch{CMD_SUFFIX}')
        self.MediaInfoCommand = getCommand('MEDIAINFO_COMMAND', f'mediainfo{CMD_SUFFIX}')
        self.HashCommand = getCommand('HASH_COMMAND', f'hash{CMD_SUFFIX}')
        self.LeechZipWatchCommand = getCommand('LEECHZIPWATCH_COMMAND', f'leechzipwatch{CMD_SUFFIX}')
        self.RssListCommand = getCommand('RSSLIST_COMMAND', f'rsslist{CMD_SUFFIX}')
        self.RssGetCommand = getCommand('RSSGET_COMMAND', f'rssget{CMD_SUFFIX}')
        self.RssSubCommand = getCommand('RSSSUB_COMMAND', f'rsssub{CMD_SUFFIX}')
        self.RssUnSubCommand = getCommand('RSSUNSUB_COMMAND', f'rssunsub{CMD_SUFFIX}')
        self.RssSettingsCommand = getCommand('RSSSET_COMMAND', f'rssset{CMD_SUFFIX}')
        self.WayBackCommand = getCommand('WAYBACK_COMMAND', f'wayback{CMD_SUFFIX}')
        self.AddleechlogCommand = getCommand('ADDLEECHLOG_CMD', f'addleechlog{CMD_SUFFIX}')
        self.RmleechlogCommand = getCommand('RMLEECHLOG_CMD', f'rmleechlog{CMD_SUFFIX}')
        self.UsageCommand = getCommand('USAGE_COMMAND', f'usage{CMD_SUFFIX}')
        self.SleepCommand = getCommand('SLEEP_COMMAND', f'sleep{CMD_SUFFIX}')
        self.EvalCommand = f'eval{CMD_SUFFIX}'
        self.ExecCommand = f'exec{CMD_SUFFIX}'
        self.ClearLocalsCommand = f'clearlocals{CMD_SUFFIX}'

BotCommands = _BotCommands()
