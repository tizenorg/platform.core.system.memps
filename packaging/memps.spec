Name:       memps
Summary:    Displays memory usage information
Version: 	0.1.8
Release:    92
Group:      System/Libraries
License:    Apache License, Version 2.0
Source0:    %{name}-%{version}.tar.gz

%description
memps displays information about current memory usage of processes, tmpfs and
Low Memory Notifier.


%prep
%setup -q


%build
make PREFIX=${_prefix} 


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/license
cp LICENSE %{buildroot}/usr/share/license/%{name}
make install DESTDIR=%{buildroot} PREFIX=%{_prefix}


for f in `find ./ -name "*.in"`; do \
    cat $f > ${f%.in}; \
sed -i -e "s#@PREFIX@#%{_prefix}#g" ${f%.in}; \
done

%files
%manifest memps.manifest
%defattr(-,root,root,-)
%{_bindir}/memps
/usr/share/license/%{name}



