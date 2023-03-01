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
        self.StartCommand = getCommand(f'START_COMMAND', f'start{CMD_SUFFIX}'), f'srt{CMD_SUFFIX}'
        self.MirrorCommand = getCommand('MIRROR_COMMAND', f'mirror{CMD_SUFFIX}'), f'm{CMD_SUFFIX}'
        self.UnzipMirrorCommand = getCommand('UNZIP_COMMAND', f'unzipmirror{CMD_SUFFIX}'), f'uzm{CMD_SUFFIX}'
        self.ZipMirrorCommand = getCommand('ZIP_COMMAND', f'zipmirror{CMD_SUFFIX}'), f'zm{CMD_SUFFIX}'
        self.CancelMirror = getCommand('CANCEL_COMMAND', f'cancel{CMD_SUFFIX}'), f'c{CMD_SUFFIX}'
        self.CancelAllCommand = getCommand(f'CANCEL_ALL_COMMAND', f'cancelall{CMD_SUFFIX}'), f'ca{CMD_SUFFIX}'
        self.ListCommand = getCommand(f'LIST_COMMAND', f'list{CMD_SUFFIX}'), f'ls{CMD_SUFFIX}'
        self.SearchCommand = getCommand('SEARCH_COMMAND', f'search{CMD_SUFFIX}')
        self.PaidUsersCommand = getCommand('PAID_COMMAND', f'paid{CMD_SUFFIX}')
        self.AddPaidCommand = getCommand('ADDPAID_COMMAND', f'addpaid{CMD_SUFFIX}')
        self.RmPaidCommand = getCommand('RMPAID_COMMAND', f'rmpaid{CMD_SUFFIX}')
        self.PreNameCommand = getCommand('PRENAME_COMMAND', f'prename{CMD_SUFFIX}'), f'pre{CMD_SUFFIX}'
        self.CaptionCommand = getCommand('CAPTION_COMMAND', f'caption{CMD_SUFFIX}'), f'cap{CMD_SUFFIX}'
        self.UserLogCommand = getCommand('DUMPID_COMMAND', f'dumpid{CMD_SUFFIX}')
        self.StatusCommand = getCommand(f'STATUS_COMMAND', f'status{CMD_SUFFIX}'), f'sts{CMD_SUFFIX}'
        self.AuthorizedUsersCommand = getCommand(f'USERS_COMMAND', f'kpsusers{CMD_SUFFIX}'), f'usr{CMD_SUFFIX}'
        self.AuthorizeCommand = getCommand(f'AUTH_COMMAND', f'kpsauthorize{CMD_SUFFIX}'), f'au{CMD_SUFFIX}'
        self.UnAuthorizeCommand = getCommand(f'UNAUTH_COMMAND', f'kpsunauthorize{CMD_SUFFIX}'), f'ua{CMD_SUFFIX}'
        self.AddSudoCommand = getCommand(f'ADDSUDO_COMMAND', f'kpsaddsudo{CMD_SUFFIX}'), f'asd{CMD_SUFFIX}'
        self.RmSudoCommand = getCommand(f'RMSUDO_COMMAND', f'kpsrmsudo{CMD_SUFFIX}'), f'rmsd{CMD_SUFFIX}'
        self.PingCommand = getCommand('PING_COMMAND', f'ping{CMD_SUFFIX}')
        self.RestartCommand =  getCommand(f'RESTART_COMMAND', f'restart{CMD_SUFFIX}'), f'rst{CMD_SUFFIX}'
        self.StatsCommand = getCommand('STATS_COMMAND', f'stats{CMD_SUFFIX}')
        self.HelpCommand = getCommand('HELP_COMMAND', f'help{CMD_SUFFIX}'), f'hlp{CMD_SUFFIX}'
        self.LogCommand = getCommand('LOG_COMMAND', f'log{CMD_SUFFIX}')
        self.BtSelectCommand = getCommand('BTSEL_COMMAND', f'btsel{CMD_SUFFIX}')
        self.SpeedCommand = getCommand('SPEEDTEST_COMMAND', f'speedtest{CMD_SUFFIX}'), f'sp{CMD_SUFFIX}'
        self.CloneCommand = getCommand('CLONE_COMMAND', f'clone{CMD_SUFFIX}'), f'cl{CMD_SUFFIX}'
        self.CountCommand = getCommand('COUNT_COMMAND', f'count{CMD_SUFFIX}')
        self.WatchCommand =  getCommand('WATCH_COMMAND', f'watch{CMD_SUFFIX}'), f'w{CMD_SUFFIX}'
        self.ZipWatchCommand = getCommand('ZIPWATCH_COMMAND', f'zipwatch{CMD_SUFFIX}'), f'zw{CMD_SUFFIX}'
        self.ScrapeCommand = getCommand('SCRAPE_COMMAND', f'scrape{CMD_SUFFIX}')
        self.QbMirrorCommand = getCommand('QBMIRROR_COMMAND', f'qbmirror{CMD_SUFFIX}'), f'qm{CMD_SUFFIX}'
        self.QbUnzipMirrorCommand = getCommand('QBUNZIP_COMMAND', f'qbunzipmirror{CMD_SUFFIX}'), f'quzm{CMD_SUFFIX}'
        self.QbZipMirrorCommand = getCommand('QBZIP_COMMAND', f'qbzipmirror{CMD_SUFFIX}'), f'qzm{CMD_SUFFIX}'
        self.DeleteCommand = getCommand('DELETE_COMMAND', f'del{CMD_SUFFIX}')
        self.ShellCommand = getCommand('SHELL_COMMAND', f'shell{CMD_SUFFIX}')
        self.ExecHelpCommand = getCommand('EXEHELP_COMMAND', f'exechelp{CMD_SUFFIX}')
        self.LeechSetCommand = getCommand('LEECHSET_COMMAND', f'leechset{CMD_SUFFIX}')
        self.SetThumbCommand = getCommand('SETTHUMB_COMMAND', f'setthumb{CMD_SUFFIX}'), f'st{CMD_SUFFIX}'
        self.UsageCommand = getCommand('USAGE_COMMAND', f'usage{CMD_SUFFIX}')
        self.LeechCommand = getCommand('LEECH_COMMAND', f'leech{CMD_SUFFIX}'), f'l{CMD_SUFFIX}'
        self.UnzipLeechCommand = getCommand('UNZIPLEECH_COMMAND', f'unzipleech{CMD_SUFFIX}'), f'uzl{CMD_SUFFIX}'
        self.ZipLeechCommand = getCommand('ZIPLEECH_COMMAND', f'zipleech{CMD_SUFFIX}'), f'zl{CMD_SUFFIX}'
        self.QbLeechCommand = getCommand('QBLEECH_COMMAND', f'qbleech{CMD_SUFFIX}'), f'ql{CMD_SUFFIX}'
        self.QbUnzipLeechCommand = getCommand('QBZIPLEECH_COMMAND', f'qbunzipleech{CMD_SUFFIX}'), f'quzl{CMD_SUFFIX}'
        self.QbZipLeechCommand = getCommand('QBUNZIPLEECH_COMMAND', f'qbzipleech{CMD_SUFFIX}'), f'qzl{CMD_SUFFIX}'
        self.LeechWatchCommand = getCommand('LEECHWATCH_COMMAND',  f'leechwatch{CMD_SUFFIX}'), f'lw{CMD_SUFFIX}'
        self.MediaInfoCommand = getCommand('MEDIAINFO_COMMAND', f'mediainfo{CMD_SUFFIX}')
        self.HashCommand = getCommand('HASH_COMMAND', f'hash{CMD_SUFFIX}')
        self.LeechZipWatchCommand = getCommand('LEECHZIPWATCH_COMMAND', f'leechzipwatch{CMD_SUFFIX}'), f'lzw{CMD_SUFFIX}'
        self.RssListCommand = getCommand('RSSLIST_COMMAND', f'rsslist{CMD_SUFFIX}')
        self.RssGetCommand = getCommand('RSSGET_COMMAND', f'rssget{CMD_SUFFIX}')
        self.RssSubCommand = getCommand('RSSSUB_COMMAND', f'rsssub{CMD_SUFFIX}')
        self.RssUnSubCommand = getCommand('RSSUNSUB_COMMAND', f'rssunsub{CMD_SUFFIX}')
        self.RssSettingsCommand = getCommand('RSSSET_COMMAND', f'rssset{CMD_SUFFIX}')
        self.WayBackCommand = getCommand('WAYBACK_COMMAND', f'wayback{CMD_SUFFIX}')
        self.SleepCommand = getCommand('SLEEP_COMMAND', f'sleep{CMD_SUFFIX}')
        self.AddleechlogCommand = getCommand('ADDLEECHLOG_CMD', f'addleechlog{CMD_SUFFIX}')
        self.RmleechlogCommand = getCommand('RMLEECHLOG_CMD', f'rmleechlog{CMD_SUFFIX}')
        self.EvalCommand = f'eval{CMD_SUFFIX}'
        self.ExecCommand = f'exec{CMD_SUFFIX}'
        self.ClearLocalsCommand = f'clearlocals{CMD_SUFFIX}'

BotCommands = _BotCommands()


