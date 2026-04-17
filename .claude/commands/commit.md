Generate a git commit following the Conventional Commits specification for the current staged changes.

1. Run `git diff --staged` to review all staged changes.
2. Run `git status` to see which files are included.
3. Determine the appropriate type, optional scope, and a concise description.
4. Create the commit using the format below.

## Commit Format

```
<type>(<scope>): <description>

[optional body]

[optional footer(s)]
```

## Types

- `feat`: A new feature
- `fix`: A bug fix
- `docs`: Documentation only changes
- `style`: Changes that do not affect the meaning of the code (white-space, formatting)
- `refactor`: A code change that neither fixes a bug nor adds a feature
- `perf`: A code change that improves performance
- `test`: Adding missing tests or correcting existing tests
- `build`: Changes that affect the build system or external dependencies
- `ci`: Changes to CI configuration files and scripts
- `chore`: Other changes that don't modify src or test files
- `revert`: Reverts a previous commit

## Rules

1. `type` is required and must be one of the types listed above.
2. `scope` is optional — a noun describing the section of the codebase (e.g., `api`, `ui`, `auth`).
3. `description` is required: lowercase, imperative tense, no period at the end.
4. A `!` after the type/scope indicates a breaking change (e.g., `feat!: remove deprecated API`).
5. Body should explain the motivation for the change.
6. Footer should contain `BREAKING CHANGE:` for breaking changes or reference issues (e.g., `Closes #123`).

## Examples

```
feat(auth): add OAuth2 login support
```

```
fix(api): handle null response from upstream service

The upstream service occasionally returns null instead of an empty array.

Closes #456
```

```
refactor!: drop support for Node 14

BREAKING CHANGE: Node 14 is no longer supported due to EOL.
```
