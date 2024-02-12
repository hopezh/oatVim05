return {
    "lukas-reineke/headlines.nvim",

    dependencies = "nvim-treesitter/nvim-treesitter",

    config = function()
        require("headlines").setup({
            quarto = {
                query = vim.treesitter.query.parse(
                    "markdown",
                    [[
                        (thematic_break) @dash
                        (fenced_code_block) @codeblock
                        (block_quote_marker) @quote
                        (block_quote (paragraph (inline (block_continuation) @quote)))
                    ]]
                ),

                treesitter_language = "markdown",

                headline_highlights = {
                    "Headline1",
                    "Headline2",
                    "Headline3",
                },
                codeblock_highlight = "CodeBlock",
                dash_highlight = "Dash",
                dash_string = "-",
                quote_highlight = "Quote",
                quote_string = "┃",
                fat_headlines = true,
                fat_headline_upper_string = "",
                fat_headline_lower_string = "",
            },

            markdown = {
                query = vim.treesitter.query.parse(
                    "markdown",
                    [[
                        (thematic_break) @dash
                        (fenced_code_block) @codeblock
                        (block_quote_marker) @quote
                        (block_quote (paragraph (inline (block_continuation) @quote)))
                    ]]
                ),

                treesitter_language = "markdown",

                -- headline_highlights = { "Headline" },
                headline_highlights = {
                    "Headline1",
                    "Headline2",
                    "Headline3",
                },
                codeblock_highlight = "CodeBlock",
                dash_highlight = "Dash",
                dash_string = "-",
                quote_highlight = "Quote",
                quote_string = "┃",
                fat_headlines = true,
                -- fat_headline_upper_string = "▃",
                -- fat_headline_lower_string = "🬂",
                fat_headline_upper_string = "",
                fat_headline_lower_string = "",
            },
        })
    end,
}
