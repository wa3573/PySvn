import wjasvn.constants
import wjasvn.common


class RemoteClient(wjasvn.common.CommonClient):

    def __init__(self, url, *args, **kwargs):
        super(RemoteClient, self).__init__(
            url,
            wjasvn.constants.LT_URL,
            *args, **kwargs)

    def checkout(self, path, revision=None):
        cmd = []
        if revision is not None:
            cmd += ['-r', str(revision)]

        cmd += [self.url, path]

        self.run_command('checkout', cmd)

    def remove(self, rel_path, message, do_force=False):
        args = [
            '--message', message,
        ]

        if do_force is True:
            args.append('--force')

        url = '{}/{}'.format(self.url, rel_path)

        args += [
            url
        ]

        self.run_command(
            'rm',
            args)

    def __repr__(self):
        return '<SVN(REMOTE) %s>' % self.url
