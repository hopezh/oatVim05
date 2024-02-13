return {
    "folke/todo-comments.nvim",

    dependencies = { "nvim-lua/plenary.nvim" },

    keys = {
        -- {
        --     "<leader>xO",
        --     "<cmd>TodoLocList keywords=oat<cr>",
        --     desc = "show oat in this project",
        -- },
        {
            "<leader>xo",
            "<cmd>TodoTrouble keywords=oat<cr>",
            desc = "show oat in Trouble",
        },
        {
            "<leader>to",
            "<cmd>TodoTelescope keywords=oat<cr>",
            desc = "show oat in Telescope",
        },
    },

    -- add custom comment keyword ----------------------------------------------
    opts = {
        merge_keywords = true,
        keywords = {
            -- oat = { icon = "", color = "#505050" },
            o = { icon = "", color = "#505050" }, -- add "# o." to activate
        },
    },
}
