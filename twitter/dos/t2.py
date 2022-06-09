from twitter import Twitter,OAuth
#Access Token,Access Token Secret,API Key,API Key Secret
t = Twitter(auth=OAuth("1229189739863068673-oWhzz3s53qBZlD1dNBIePt12m6wmx4","gXgLxKwRrs37AqGkEuLWxiFV6XheQan8lh0qV4g1XgvVo"
,"d7hb5XXA8W17Ujtez3SJAlw4B","r8SrqsbBos30iz7xTcf94mEOtOnODbOCvBq1smas30S0ut25kj"))

t.statuses.update(status='hello maalej and lahmandi!')
