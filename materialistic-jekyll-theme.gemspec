Gem::Specification.new do |spec|
  spec.name          = "materialistic-jekyll-theme"
  spec.version       = "0.1.0"
  spec.authors       = ["toxicoder"]
  spec.email         = ["toxicoder@users.noreply.github.com"]

  spec.summary       = "A Material Design 3 Jekyll theme for technical documentation."
  spec.homepage      = "https://github.com/toxicoder/materialistic-jekyll"
  spec.license       = "MIT"

  spec.files         = `git ls-files -z`.split("\x0").select do |f|
    f.match(%r{^(_layouts|_includes|_sass|assets|_data/palettes\.yml|LICENSE|README\.md)})
  end

  spec.add_runtime_dependency "jekyll", "~> 4.3"
  spec.add_runtime_dependency "jekyll-seo-tag"
  spec.add_runtime_dependency "jekyll-sitemap"
  spec.add_runtime_dependency "jekyll-feed"

  spec.add_development_dependency "bundler"
  spec.add_development_dependency "rake"
end
