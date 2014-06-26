Contributing to diversitydatapledge.org
=======================

## Contributing

The easiest way to contribute is to file an issue in [Github][https://github.com/doubleunion/opendiversitydata/issues].
If you're interested in contributing via pull request, read on.

All the data is managed through a series of [Yaml][yaml] files so it may be useful to read
up on the Yaml syntax.

To add a new company, go to the [data files](_data/) and get familiar with
how it is set up. There is a section and corresponding file for each category and they all follow this
syntax:

### Guidelines

1. **Use a Nice Icon**: The icon must be 32x32 in dimension.

### New Companies

The values should be pretty straight forward for adding a new company. The
`companies` array should already be defined, just add a new company to it like
this example:

```yml
    companies:
        - name: Company Name
          url: https://www.company.com/
          twitter: CompanyTwitter
          img: company.png
          data: Yes
          eeo-1: Yes
          date-updated: 201X
          documentation: <link to company's diversity data>
```

### New Industries

To add a new category / industry of company, modify the `industry` value in [main.yml](_data/main.yml)
and follow the template below:

```yml
sections:
  - id: industry-id
    title: Industry Name
    icon: icon-class
```

#### Pro Tips

- See Guideline #1 about icons. The png file should go in the corresponding `img/section` folder.

- For the sake of organization and readability, it is appreciated if you insert new companies alphabetically and
that your company chunk follow the same order as the example above.

- If a site does not have data available but there is documentation that they are working on releasing it, then use:

  ```yml
  data: no
  status: <url to documentation>
  ```
  
### Other Countries

This site is focused on US companies, as there is a standard document format available. If your country has a standard format analogous to the EEO-1, please file an issue as we will be refactoring the site to add more countries.

[yaml]: http://www.yaml.org/
