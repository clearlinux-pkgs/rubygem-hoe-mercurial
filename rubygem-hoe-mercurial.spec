#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-hoe-mercurial
Version  : 1.4.1
Release  : 6
URL      : https://rubygems.org/downloads/hoe-mercurial-1.4.1.gem
Source0  : https://rubygems.org/downloads/hoe-mercurial-1.4.1.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
BuildRequires : ruby
BuildRequires : rubygem-hoe
BuildRequires : rubygem-minitest
BuildRequires : rubygem-rake
BuildRequires : rubygem-rdoc
BuildRequires : rubygem-test-unit

%description
= (Another) Mercurial Plugin for hoe
* http://bitbucket.org/ged/hoe-mercurial
== Description

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n hoe-mercurial-1.4.1
gem spec %{SOURCE0} -l --ruby > rubygem-hoe-mercurial.gemspec

%build
gem build rubygem-hoe-mercurial.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
hoe-mercurial-1.4.1.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=intel.com,localhost
pushd %{buildroot}%{gem_dir}/gems/hoe-mercurial-1.4.1
rake --trace test TESTOPTS="-v"
popd


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.2.0/cache/hoe-mercurial-1.4.1.gem
/usr/lib64/ruby/gems/2.2.0/doc/hoe-mercurial-1.4.1/ri/Hoe/Mercurial/cdesc-Mercurial.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-mercurial-1.4.1/ri/Hoe/Mercurial/check_history_on_release-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-mercurial-1.4.1/ri/Hoe/Mercurial/define_mercurial_tasks-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-mercurial-1.4.1/ri/Hoe/Mercurial/get_unhistoried_version_tags-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-mercurial-1.4.1/ri/Hoe/Mercurial/hg_release_tag_prefix-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-mercurial-1.4.1/ri/Hoe/Mercurial/hg_sign_tags-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-mercurial-1.4.1/ri/Hoe/Mercurial/initialize_mercurial-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-mercurial-1.4.1/ri/Hoe/MercurialHelpers/cdesc-MercurialHelpers.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-mercurial-1.4.1/ri/Hoe/MercurialHelpers/delete_extra_files-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-mercurial-1.4.1/ri/Hoe/MercurialHelpers/edit_commit_log-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-mercurial-1.4.1/ri/Hoe/MercurialHelpers/get_current_rev-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-mercurial-1.4.1/ri/Hoe/MercurialHelpers/get_manifest-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-mercurial-1.4.1/ri/Hoe/MercurialHelpers/get_numeric_rev-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-mercurial-1.4.1/ri/Hoe/MercurialHelpers/get_repo_paths-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-mercurial-1.4.1/ri/Hoe/MercurialHelpers/get_tags-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-mercurial-1.4.1/ri/Hoe/MercurialHelpers/get_tip_info-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-mercurial-1.4.1/ri/Hoe/MercurialHelpers/get_uncommitted_files-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-mercurial-1.4.1/ri/Hoe/MercurialHelpers/get_unknown_files-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-mercurial-1.4.1/ri/Hoe/MercurialHelpers/hg_ignore_files-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-mercurial-1.4.1/ri/Hoe/MercurialHelpers/make_changelog-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-mercurial-1.4.1/ri/Hoe/MercurialHelpers/make_commit_log-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-mercurial-1.4.1/ri/Hoe/RakeHelpers/ansi_code-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-mercurial-1.4.1/ri/Hoe/RakeHelpers/ask_for_confirmation-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-mercurial-1.4.1/ri/Hoe/RakeHelpers/cdesc-RakeHelpers.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-mercurial-1.4.1/ri/Hoe/RakeHelpers/colorize-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-mercurial-1.4.1/ri/Hoe/RakeHelpers/edit-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-mercurial-1.4.1/ri/Hoe/RakeHelpers/error-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-mercurial-1.4.1/ri/Hoe/RakeHelpers/error_message-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-mercurial-1.4.1/ri/Hoe/RakeHelpers/get_target_args-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-mercurial-1.4.1/ri/Hoe/RakeHelpers/humanize_file_list-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-mercurial-1.4.1/ri/Hoe/RakeHelpers/log-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-mercurial-1.4.1/ri/Hoe/RakeHelpers/make_prompt_string-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-mercurial-1.4.1/ri/Hoe/RakeHelpers/prompt-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-mercurial-1.4.1/ri/Hoe/RakeHelpers/prompt_for_confirmation-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-mercurial-1.4.1/ri/Hoe/RakeHelpers/prompt_for_multiple_values-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-mercurial-1.4.1/ri/Hoe/RakeHelpers/prompt_with_default-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-mercurial-1.4.1/ri/Hoe/RakeHelpers/quotelist-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-mercurial-1.4.1/ri/Hoe/RakeHelpers/read_command_output-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-mercurial-1.4.1/ri/Hoe/RakeHelpers/run-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-mercurial-1.4.1/ri/Hoe/RakeHelpers/trace-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-mercurial-1.4.1/ri/Hoe/cdesc-Hoe.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-mercurial-1.4.1/ri/Object/cdesc-Object.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-mercurial-1.4.1/ri/Object/readline-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-mercurial-1.4.1/ri/cache.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-mercurial-1.4.1/ri/page-History_rdoc.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-mercurial-1.4.1/ri/page-Manifest_txt.ri
/usr/lib64/ruby/gems/2.2.0/doc/hoe-mercurial-1.4.1/ri/page-README_rdoc.ri
/usr/lib64/ruby/gems/2.2.0/gems/hoe-mercurial-1.4.1/ChangeLog
/usr/lib64/ruby/gems/2.2.0/gems/hoe-mercurial-1.4.1/History.rdoc
/usr/lib64/ruby/gems/2.2.0/gems/hoe-mercurial-1.4.1/Manifest.txt
/usr/lib64/ruby/gems/2.2.0/gems/hoe-mercurial-1.4.1/README.rdoc
/usr/lib64/ruby/gems/2.2.0/gems/hoe-mercurial-1.4.1/Rakefile
/usr/lib64/ruby/gems/2.2.0/gems/hoe-mercurial-1.4.1/lib/hoe/mercurial.rb
/usr/lib64/ruby/gems/2.2.0/specifications/hoe-mercurial-1.4.1.gemspec