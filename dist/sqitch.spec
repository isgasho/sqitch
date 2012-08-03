Name:           sqitch
Version:        0.82
Release:        1%{?dist}
Summary:        Sane database change management
License:        MIT
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/App-Sqitch-0.82/
Source0:        http://www.cpan.org/modules/by-module/App/App-Sqitch-%{version}-TRIAL.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl >= 1:v5.10.1
BuildRequires:  perl(Capture::Tiny) >= 0.12
BuildRequires:  perl(Config)
BuildRequires:  perl(Config::GitLike) >= 1.07
BuildRequires:  perl(DateTime)
BuildRequires:  perl(DBI)
BuildRequires:  perl(Digest::SHA1)
BuildRequires:  perl(File::HomeDir)
BuildRequires:  perl(Hash::Merge)
BuildRequires:  perl(IO::Pager)
BuildRequires:  perl(IPC::System::Simple) >= 1.17
BuildRequires:  perl(Locale::TextDomain) >= 1.20
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Moose) >= 2.0300
BuildRequires:  perl(Moose::Meta::TypeConstraint::Parameterizable) >= 2.0300
BuildRequires:  perl(Moose::Util::TypeConstraints) >= 2.0300
BuildRequires:  perl(MooseX::Types::Path::Class) >= 0.05
BuildRequires:  perl(namespace::autoclean) >= 0.11
BuildRequires:  perl(Path::Class)
BuildRequires:  perl(Role::HasMessage) >= 0.005
BuildRequires:  perl(Role::Identifiable::HasIdent) >= 0.005
BuildRequires:  perl(Role::Identifiable::HasTags) >= 0.005
BuildRequires:  perl(StackTrace::Auto)
BuildRequires:  perl(String::Formatter)
BuildRequires:  perl(Sub::Exporter)
BuildRequires:  perl(Sub::Exporter::Util)
BuildRequires:  perl(Template::Tiny) >= 0.11
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Dir)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::File)
BuildRequires:  perl(Test::File::Contents) >= 0.05
BuildRequires:  perl(Test::MockModule) >= 0.05
BuildRequires:  perl(Test::More) >= 0.94
BuildRequires:  perl(Test::NoWarnings) >= 0.083
BuildRequires:  perl(Test::Pod) >= 1.40
BuildRequires:  perl(Throwable)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(URI)
Requires:       perl(Config)
Requires:       perl(Config::GitLike) >= 1.07
Requires:       perl(DateTime)
Requires:       perl(DBI)
Requires:       perl(Digest::SHA1)
Requires:       perl(File::HomeDir)
Requires:       perl(Hash::Merge)
Requires:       perl(IO::Pager)
Requires:       perl(IPC::System::Simple) >= 1.17
Requires:       perl(Locale::TextDomain) >= 1.20
Requires:       perl(Moose) >= 2.0300
Requires:       perl(Moose::Meta::TypeConstraint::Parameterizable) >= 2.0300
Requires:       perl(Moose::Util::TypeConstraints) >= 2.0300
Requires:       perl(MooseX::Types::Path::Class) >= 0.05
Requires:       perl(namespace::autoclean) >= 0.11
Requires:       perl(parent)
Requires:       perl(Path::Class)
Requires:       perl(Role::HasMessage) >= 0.005
Requires:       perl(Role::Identifiable::HasIdent) >= 0.005
Requires:       perl(Role::Identifiable::HasTags) >= 0.005
Requires:       perl(StackTrace::Auto)
Requires:       perl(String::Formatter)
Requires:       perl(Sub::Exporter)
Requires:       perl(Sub::Exporter::Util)
Requires:       perl(Template::Tiny) >= 0.11
Requires:       perl(Test::Pod) >= 1.40
Requires:       perl(Throwable)
Requires:       perl(Try::Tiny)
Requires:       perl(URI)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%define etcdir %(%{__perl} -MConfig -E 'say "$Config{prefix}/etc"')

%description
This application, `sqitch`, provides a simple yet robust interface for
database change management. The philosophy and functionality is inspired by
Git.

%prep
%setup -q -n App-Sqitch-%{version}-TRIAL

%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
rm -rf $RPM_BUILD_ROOT

./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes etc META.json priv README.md
%{perl_vendorlib}/*
%{_mandir}/man3/*
%{_bindir}/*
%{etcdir}/*

%changelog
* Fri Aug 03 2012 David E. Wheeler <david.wheeler@iovation.com> TRIAL-1
- Specfile autogenerated by cpanspec 1.78.
