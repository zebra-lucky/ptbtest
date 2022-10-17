# -*- coding: utf-8 -*-
from telegram import File


class MockFile(File):

    def download(self, custom_path=None, out=None, timeout=None):
        if self.file_id not in self.bot._fdata:
            raise Exception(f'Mockbot._fdata for file_id {self.file_id}'
                            f' not found')
        fio = self.bot._fdata[self.file_id]
        if out:
            out.write(fio.read())
            return out
        elif custom_path:
            with open(custom_path, 'wb') as fd:
                fd.write(fio.read())
            return custom_path
        else:
            raise ValueError('one of custom_path or out must be presented')

    def download_as_bytearray(self, buf=None):
        if self.file_id not in self.bot._fdata:
            raise Exception(f'Mockbot._fdata for file_id {self.file_id}'
                            f' not found')
        fio = self.bot._fdata[self.file_id]
        if buf is None:
            buf = bytearray()
            buf.extend(fio.read())
        return buf
