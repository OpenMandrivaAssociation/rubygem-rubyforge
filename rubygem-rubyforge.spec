%define	oname	rubyforge

Summary:	A script which automates a limited set of rubyforge operations
Name:		rubygem-%{oname}
Version:	2.0.3
Release:	%mkrel 2
License:	MIT
Group:		Development/Ruby
URL:		http://%{oname}.rubyforge.org/
Source0:	http://gems.rubyforge.org/gems/%{oname}-%{version}.gem
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	ruby-RubyGems
Requires:	rubygem-json_pure
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
gem install --local --install-dir %{buildroot}/%{ruby_gemdir} --force %{SOURCE0}
mv %{buildroot}%{ruby_gemdir}/bin %{buildroot}%{_prefix}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc %{ruby_gemdir}/doc/%{oname}-%{version}
%{_bindir}/rubyforge
%{ruby_gemdir}/cache/%{oname}-%{version}.gem
%{ruby_gemdir}/gems/%{oname}-%{version}
%{ruby_gemdir}/specifications/%{oname}-%{version}.gemspec

