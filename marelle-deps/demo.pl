meta_pkg('widelanguagedemo', [
    '__ufw app rules',
    'python-dev',
    'python-virtualenv',
    'build-essential',
    'supervisor',
    'libevent-dev',
    '__demo_checked_out'
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
depends('__ufw app rules', _, ['ufw core rules']).

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
    bash('git checkout https://github.com/larsyencken/wide-language-demo'),
    bash('cd wide-language-demo && git submodule init && git submodule update').
