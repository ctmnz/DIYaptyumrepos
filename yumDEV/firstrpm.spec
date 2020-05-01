Name:       firstrpm
Version:    1
Release:    1
Summary:    Most simple RPM package
License:    FIXME

%description
This is my first RPM package, which does nothing.

%prep
# we have no source, so nothing here

%build
cat > firstrpm.sh <<EOF
#!/usr/bin/bash
echo Hello from the firstrpm
EOF

%install
mkdir -p %{buildroot}/usr/bin/
install -m 755 firstrpm.sh %{buildroot}/usr/bin/firstrpm.sh

%files
/usr/bin/firstrpm.sh

%changelog
# let's skip this for now
