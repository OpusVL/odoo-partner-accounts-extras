alter table account_move_line drop column if exists amount_residual_agg;
alter table account_move_line drop column if exists amount_residual_currency_agg;
