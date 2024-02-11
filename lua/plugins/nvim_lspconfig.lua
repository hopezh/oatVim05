return {
    "neovim/nvim-lspconfig",

    ---@class PluginLspOpts
    opts = {
        ---@type lspconfig.options
        servers = {
            pyright = {},
            -- r_language_server = {},
            -- julials = {},
            marksman = {
                -- also need to add the following two lines:
                --      [core]
                --      markdown.file_extensions = ["md", "markdown", "qmd"]
                -- to $home/.config/marksman/config.toml in Mac OS
                -- to $home\AppData\Roaming\marksman\config.toml in Windows
                filetypes = { "markdown", "quarto" },
                root_dir = require("lspconfig.util").root_pattern(".git", ".marksman.toml", "_quarto.yml"),
            },
        },
    },
}
