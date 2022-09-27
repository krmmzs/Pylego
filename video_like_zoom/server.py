#!/usr/bin python3

import numpy as np
from jina import Executor, requests, Flow


class VideoChatExecutor(Executor):
    last_user_frame = {}

    @requests
    def foo(self, docs, **kwargs):
        for d in docs:
            self.last_user_frame[d.tags["user"]] = d.tensor
        if len(self.last_user_frame) > 1:
            d.tensor = np.concatenate(list(self.last_user_frame.values()), axis=0)


f = Flow().add(uses=VideoChatExecutor)

with f:
    f.block()
