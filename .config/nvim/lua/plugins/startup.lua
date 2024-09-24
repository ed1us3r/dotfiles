return{
  { url = "git@github.com:mong8se/actually.nvim.git" },
  {
    "startup-nvim/startup.nvim",
    dependencies = { "nvim-telescope/telescope.nvim", "nvim-lua/plenary.nvim", "nvim-telescope/telescope-file-browser.nvim" },
    config = function()
      require "startup".setup()
    end
  }
  {
    "nvim-neo-tree/neo-tree.nvim",
      opts = {
        filesystem = {
          filtered_items = {
      visible = true,
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