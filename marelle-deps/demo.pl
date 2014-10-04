meta_pkg('widelanguagedemo', [
    '__ufw app rules',
    'python-dev',
    'python-virtualenv',
    'build-essential',
    'supervisor',
    'libevent-dev',
    '__data checked out',
    '__supervisor configured',
    '__allow python to listen on port 80'
]).

pkg('__ufw core rules').
met('__ufw core rules', _) :- isfile('~/.ufw_created').
meet('__ufw core rules', _) :-
    bash('sudo ufw default deny'),
    bash('sudo ufw allow from any to any port 22'),
    bash('sudo ufw enable'),
    bash('touch ~/.ufw_created').
depends('__ufw core rules', _, [ufw]).

pkg('__ufw app rules').
met('__ufw app rules', _) :- isfile('~/.ufw_app').
meet('__ufw app rules', _) :-
    bash('sudo ufw allow from any to any port 80'),
    bash('touch ~/.ufw_app').
depends('__ufw app rules', _, ['__ufw core rules']).

managed_pkg(ufw).
managed_pkg(mongodb).
managed_pkg('python-dev').
managed_pkg('python-virtualenv').
managed_pkg('build-essential').
managed_pkg('supervisor').
managed_pkg('libevent-dev').

managed_pkg(screen).
managed_pkg('vim-nox').
managed_pkg(htop).

pkg('__demo checked out').
met('__demo checked out', _) :- isdir('~/wide-language-demo').
meet('__demo checked out', _) :-
    bash('git checkout https://github.com/larsyencken/wide-language-demo').

pkg('__data checked out').
met('__data checked out', _) :- isdir('~/wide-language-demo/widelanguagedemo/index/data/index').
meet('__data checked out', _) :-
    bash('cd wide-language-demo && git submodule init && git submodule update').
depends('__data checked out', _,  ['__demo checked out']).

pkg('__supervisor configured').
met('__supervisor configured', _) :-
    isfile('/etc/supervisor/conf.d/widelanuagedemo.conf'),
    bash('diff -q /etc/supervisor/conf.d/widelanuagedemo.conf /home/ubuntu/wide-language-demo/ops/widelanguagedemo.conf').
meet('__supervisor configured', _) :-
    bash('sudo cp -f /home/ubuntu/wide-language-demo/ops/widelanguagedemo.conf /etc/supervisor/conf.d/widelanuagedemo.conf'),
    bash('sudo service supervisor stop'),
    bash('sudo service supervisor start').

pkg('__allow python to listen on port 80').
met('__allow python to listen on port 80', _) :-
    bash('sudo getcap /tmp/virtualenv/widelanguagedemo/bin/python | fgrep "cap_net_bind_service+ep"').
meet('__allow python to listen on port 80', _) :-
    bash('sudo setcap cap_net_bind_service+ep /tmp/virtualenv/widelanguagedemo/bin/python').
depends('__allow python to listen on port 80', _, ['libcap2-bin']).

managed_pkg('libcap2-bin').
