%define	oname	rubyforge

Summary:	A script which automates a limited set of rubyforge operations
Name:		rubygem-%{oname}
Version:	2.0.4
Release:	2
License:	MIT
Group:		Development/Ruby
URL:		https://%{oname}.rubyforge.org/
Source0:	http://gems.rubyforge.org/gems/%{oname}-%{version}.gem
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	ruby-RubyGems
BuildArch:	noarch

%description
A script which automates a limited set of rubyforge operations.

* Run 'rubyforge help' for complete usage.
* Setup: For first time users AND upgrades to 0.4.0:
  * rubyforge setup (deletes your username and password, so run sparingly!)
  * edit ~/.rubyforge/user-config.yml
  * rubyforge config
* For all rubyforge upgrades, run 'rubyforge config' to ensure you have latest.

%prep

%build

%install
rm -rf %{buildroot}
gem install -E -n %{buildroot}%{_bindir} --local --install-dir %{buildroot}/%{ruby_gemdir} --force %{SOURCE0}
rm -rf %{buildroot}%{ruby_gemdir}/{cache,gems/%{oname}-%{version}/ext}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc %{ruby_gemdir}/doc/%{oname}-%{version}
%{_bindir}/rubyforge
%{ruby_gemdir}/gems/%{oname}-%{version}
%{ruby_gemdir}/specifications/%{oname}-%{version}.gemspec



%changelog
* Sat Sep 18 2010 Per Øyvind Karlsen <peroyvind@mandriva.org> 2.0.4-1mdv2011.0
+ Revision: 579405
- new release: 2.0.4
- don't install gem archive
- rebuild for new automatic requires/provides

* Wed Feb 03 2010 Per Øyvind Karlsen <peroyvind@mandriva.org> 2.0.3-1mdv2010.1
+ Revision: 500339
- import rubygem-rubyforge


* Mon Feb  3 2010 Per Øyvind Karlsen <peroyvind@mandriva.org> 2.0.3-1
- initial release
