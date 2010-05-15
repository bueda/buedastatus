<html>
<head>
<title>Bueda Status</title>
</head>
<body>
% for s in c.statuses:
    <p>At ${s.time}: ${s.status}</p>
% endfor

<a href="/page/${c.page + 1}">Next page</a>
</body>
</html>

