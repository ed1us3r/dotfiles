return{
  { url = "git@github.com:mong8se/actually.nvim.git" },
  {
    "nvim-neo-tree/neo-tree.nvim",
      opts = {
        filesystem = {
          filtered_items = {
      visible = true,
      dependencies = {
      	"nvim-lua/plenary.nvim",
     	"nvim-tree/nvim-web-devicons", -- not strictly required, but recommended
     	"MunifTanjim/nui.nvim",
      	-- "3rd/image.nvim", -- Optional image support in preview window: See `# Preview Mode` for more information
    },
      show_hidden_count = true,
      hide_dotfiles = false,
      hide_gitignored = true,
      hide_by_name = {
        -- '.git',
        -- '.DS_Store',
        -- 'thumbs.db',
      },
      never_show = {},
          },
        }
      }
  }
}
