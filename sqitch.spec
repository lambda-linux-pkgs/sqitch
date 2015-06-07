%define _buildid .1

Name:           sqitch
Version:        0.9992
Release:        1%{?_buildid}%{?dist}
Summary:        Sane database change management
License:        MIT
Group:          Development/Libraries
URL:            http://sqitch.org/
Source0:        http://www.cpan.org/modules/by-module/App/App-Sqitch-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl >= 1:v5.10.0
BuildRequires:  perl(Capture::Tiny) >= 0.12
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::XSAccessor) >= 1.18
BuildRequires:  perl(Clone)
BuildRequires:  perl(Config)
BuildRequires:  perl(Config::GitLike) >= 1.11
BuildRequires:  perl(constant)
BuildRequires:  perl(DateTime)
BuildRequires:  perl(DateTime::TimeZone)
BuildRequires:  perl(DBI)
BuildRequires:  perl(Devel::StackTrace) >= 1.30
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Encode::Locale)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::HomeDir)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Hash::Merge)
BuildRequires:  perl(IO::Pager)
BuildRequires:  perl(IPC::Run3)
BuildRequires:  perl(IPC::System::Simple) >= 1.17
BuildRequires:  perl(List::Util)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(Locale::TextDomain) >= 1.20
BuildRequires:  perl(Module::Build) >= 0.35
BuildRequires:  perl(Moo) >= 1.002000
BuildRequires:  perl(Moo::Role)
BuildRequires:  perl(Moo::sification)
BuildRequires:  perl(namespace::autoclean) >= 0.16
BuildRequires:  perl(parent)
BuildRequires:  perl(overload)
BuildRequires:  perl(Path::Class) >= 0.33
BuildRequires:  perl(PerlIO::utf8_strict)
BuildRequires:  perl(Pod::Find)
BuildRequires:  perl(Pod::Usage)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(StackTrace::Auto)
BuildRequires:  perl(strict)
BuildRequires:  perl(String::Formatter)
BuildRequires:  perl(String::ShellQuote)
BuildRequires:  perl(Sub::Exporter)
BuildRequires:  perl(Sub::Exporter::Util)
BuildRequires:  perl(Sys::Hostname)
BuildRequires:  perl(Template::Tiny) >= 0.11
BuildRequires:  perl(Term::ANSIColor) >= 2.02
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Dir)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::File)
BuildRequires:  perl(Test::File::Contents) >= 0.20
BuildRequires:  perl(Test::MockModule) >= 0.05
BuildRequires:  perl(Test::More) >= 0.94
BuildRequires:  perl(Test::NoWarnings) >= 0.083
BuildRequires:  perl(Throwable) >= 0.200009
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(Type::Library) >= 0.040
BuildRequires:  perl(Type::Tiny::XS) >= 0.010
BuildRequires:  perl(Type::Utils)
BuildRequires:  perl(Types::Standard)
BuildRequires:  perl(URI)
BuildRequires:  perl(URI::db) >= 0.15
BuildRequires:  perl(User::pwent)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
Requires:       perl(Class::XSAccessor) >= 1.18
Requires:       perl(Clone)
Requires:       perl(Config)
Requires:       perl(Config::GitLike) >= 1.11
Requires:       perl(constant)
Requires:       perl(DateTime)
Requires:       perl(DateTime::TimeZone)
Requires:       perl(Devel::StackTrace) >= 1.30
Requires:       perl(Digest::SHA)
Requires:       perl(Encode)
Requires:       perl(Encode::Locale)
Requires:       perl(File::Basename)
Requires:       perl(File::Copy)
Requires:       perl(File::HomeDir)
Requires:       perl(File::Path)
Requires:       perl(File::Temp)
Requires:       perl(Getopt::Long)
Requires:       perl(Hash::Merge)
Requires:       perl(IO::Pager)
Requires:       perl(IPC::Run3)
Requires:       perl(IPC::System::Simple) >= 1.17
Requires:       perl(List::Util)
Requires:       perl(List::MoreUtils)
Requires:       perl(Locale::TextDomain) >= 1.20
Requires:       perl(Moo) => 1.002000
Requires:       perl(Moo::Role)
Requires:       perl(Moo::sification)
Requires:       perl(namespace::autoclean) >= 0.16
Requires:       perl(parent)
Requires:       perl(overload)
Requires:       perl(Path::Class)
Requires:       perl(PerlIO::utf8_strict)
Requires:       perl(Pod::Find)
Requires:       perl(Pod::Usage)
Requires:       perl(POSIX)
Requires:       perl(Scalar::Util)
Requires:       perl(StackTrace::Auto)
Requires:       perl(strict)
Requires:       perl(String::Formatter)
Requires:       perl(String::ShellQuote)
Requires:       perl(Sub::Exporter)
Requires:       perl(Sub::Exporter::Util)
Requires:       perl(Sys::Hostname)
Requires:       perl(Template::Tiny) >= 0.11
Requires:       perl(Term::ANSIColor) >= 2.02
Requires:       perl(Throwable) >= 0.200009
Requires:       perl(Try::Tiny)
Requires:       perl(Type::Library) >= 0.040
Requires:       perl(Type::Tiny::XS) >= 0.010
Requires:       perl(Type::Utils)
Requires:       perl(Types::Standard)
Requires:       perl(URI)
Requires:       perl(URI::db) >= 0.15
Requires:       perl(User::pwent)
Requires:       perl(utf8)
Requires:       perl(warnings)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%define etcdir %(%{__perl} -MConfig -E 'say "$Config{prefix}/etc"')

%description
For package support, please visit
https://github.com/lambda-linux-pkgs/%{name}/issues

This application, `sqitch`, provides a simple yet robust interface for
database change management. The philosophy and functionality is inspired by
Git.

%prep
%setup -q -n App-Sqitch-%{version}

%build
%{__perl} Build.PL installdirs=vendor destdir=$RPM_BUILD_ROOT
./Build

%install
rm -rf $RPM_BUILD_ROOT

./Build install create_packlist=0
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes META.json README.md
%{perl_vendorlib}/*
%{_mandir}/man3/*
%{_bindir}/*
%config %{etcdir}/*

%package pg
Summary:        Sane database change management for PostgreSQL
Group:          Development/Libraries
Requires:       sqitch >= %{version}
Requires:       postgresql >= 8.4.0
Requires:       perl(DBI)
Requires:       perl(DBD::Pg) >= 2.0.0

%description pg
For package support, please visit
https://github.com/lambda-linux-pkgs/%{name}/issues

Sqitch provides a simple yet robust interface for database change
management. The philosophy and functionality is inspired by Git. This
package bundles the Sqitch PostgreSQL support.

%files pg
# No additional files required.

%package sqlite
Summary:        Sane database change management for SQLite
Group:          Development/Libraries
Requires:       sqitch >= %{version}
Requires:       sqlite
Requires:       perl(DBI)
Requires:       perl(DBD::SQLite) >= 1.37

%description sqlite
For package support, please visit
https://github.com/lambda-linux-pkgs/%{name}/issues

Sqitch provides a simple yet robust interface for database change
management. The philosophy and functionality is inspired by Git. This
package bundles the Sqitch SQLite support.

%files sqlite
# No additional files required.

%package oracle
Summary:        Sane database change management for Oracle
Group:          Development/Libraries
Requires:       sqitch >= %{version}
Requires:       perl(DBI)

%description oracle
For package support, please visit
https://github.com/lambda-linux-pkgs/%{name}/issues

Sqitch provides a simple yet robust interface for database change
management. The philosophy and functionality is inspired by Git. This
package bundles the Sqitch Oracle support.

%files oracle
# No additional files required.

%posttrans oracle -p <lua>
msg = [[

SQITCH ORACLE POST INSTALLATION NOTES
-------------------------------------

Thank you for installing `sqitch-oracle`.

Unfortunately due to licensing issues, we cannot
provide Oracle Instant Client RPMs in our
repositories.

Therefore, please go to,

http://www.oracle.com/technetwork/topics/linuxx86-64soft-092277.html

and download the following packages.

- oracle-instantclient11.2-basic-11.2.0.4.0-1.x86_64.rpm
- oracle-instantclient11.2-sqlplus-11.2.0.4.0-1.x86_64.rpm

You can install the packages using the following
command in the directory where you've downloaded
the packages,

```
$ sudo yum install ./oracle-instantclient11.2-*.x86_64.rpm
```

Once the installation of Oracle Instant Client is
complete, please install `perl-DBD-Oracle` package
which is needed by `sqitch-oracle`.

You can do this using the following command,

```
$ sudo yum --enablerepo=epll install perl-DBD-Oracle
```

This will complete your installation of
`sqitch-oracle` package.

]]
print(msg)

%package mysql
Summary:        Sane database change management for MySQL
Group:          Development/Libraries
Requires:       sqitch >= %{version}
Requires:       mysql >= 5.5.40
Requires:       perl(DBI)
Requires:       perl(DBD::mysql) >= 4.018
Requires:       perl(MySQL::Config)

%description mysql
For package support, please visit
https://github.com/lambda-linux-pkgs/%{name}/issues

Sqitch provides a simple yet robust interface for database change
management. The philosophy and functionality is inspired by Git. This
package bundles the Sqitch MySQL support.

%files mysql
# No additional files required.

%changelog
* Mon Jan 05 2015 Rajiv M Ranganath <rajiv.ranganath@atihita.com> 0.997-1
- Adapt for AL/LL
- Add package support URL
- Update `sqitch-oracle` and add `%posttrans` notes
- Update `sqitch-mysql` requires
- Disable `firebird` and `vertica` support
- Cleanup `%changelog`
- Import `App-Sqitch-0.997.tar.gz`
- Import spec file

* Tue Nov 4 2014 David E. Wheeler <david.wheeler@iovation.com> 0.997-1
- Upgrade to v0.997.

* Fri Sep 5 2014 David E. Wheeler <david.wheeler@iovation.com> 0.996-1
- Upgrade to v0.996.
- Remove Moose and Mouse dependencies.
- Add Moo dependencies.
- Add Type::Library and related module dependencies.
- Switch from Digest::SHA1 to Digest::SHA.
- Require the Moo-backed version of Config::GitLike.
- Remove Role module dependencies.
- Require URI::db v0.15.
- Add sqitch-vertica.
