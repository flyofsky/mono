class FsharpPackage(GitHubTarballPackage):
	def __init__(self):
		GitHubTarballPackage.__init__(self,
			'fsharp', 'fsharp',
			'4.1.24',
			'7975efc3989888603a6169238ac0fa4671c2fceb',
			configure = './configure --prefix="%{package_prefix}"',
			override_properties = { 'make': 'make' })

		self.extra_stage_files = ['lib/mono/xbuild/Microsoft/VisualStudio/v/FSharp/Microsoft.FSharp.Targets']
		self.sources.extend (['patches/fsharp-enable-jit-tracking-for-portable-pdb.patch', 'patches/fsharp-fix-mdb-support.patch', 'patches/fsharp-Fix-mono-gac-location.patch', 'patches/fsharp-fix-xbuild-check.patch', 'patches/fsharp-use-standard-resource-names.patch'])

	def prep(self):
		Package.prep (self)

		for p in range (1, len (self.sources)):
				self.sh ('patch -p1 < "%{local_sources[' + str (p) + ']}"')

	def build(self):
		self.sh ('autoreconf')
		Package.configure (self)
		Package.make (self)

FsharpPackage()
