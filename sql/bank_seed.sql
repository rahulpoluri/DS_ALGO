-- Practice schema: open-banking style (customers = Qwist clients, end users, accounts, transactions)
DROP TABLE IF EXISTS transactions, accounts, end_users, customers CASCADE;

CREATE TABLE customers (            -- B2B clients of the API (lenders, fintechs)
  id   serial PRIMARY KEY,
  name text NOT NULL
);
CREATE TABLE end_users (            -- people who gave consent
  id          serial PRIMARY KEY,
  customer_id int NOT NULL REFERENCES customers(id),
  name        text NOT NULL
);
CREATE TABLE accounts (
  id          serial PRIMARY KEY,
  end_user_id int NOT NULL REFERENCES end_users(id),
  bank_name   text NOT NULL,
  iban        text NOT NULL UNIQUE,
  currency    char(3) NOT NULL DEFAULT 'EUR'
);
CREATE TABLE transactions (
  id            bigserial PRIMARY KEY,
  account_id    int NOT NULL REFERENCES accounts(id),
  bank_tx_id    text,                -- id the BANK gave it (duplicates possible after re-sync!)
  booking_date  date NOT NULL,
  amount        numeric(12,2) NOT NULL,   -- negative = money out
  counterparty  text,
  category      text                -- NULL = not categorised yet
);

INSERT INTO customers (name) VALUES ('LendFast'), ('AutoFinance');
INSERT INTO end_users (customer_id, name) VALUES (1,'Anna'), (1,'Ben'), (2,'Chen'), (2,'Dita');
INSERT INTO accounts (end_user_id, bank_name, iban) VALUES
 (1,'DKB','DE01'), (1,'Sparkasse','DE02'), (2,'DKB','DE03'), (3,'N26','DE04'), (4,'Commerzbank','DE05');

INSERT INTO transactions (account_id, bank_tx_id, booking_date, amount, counterparty, category) VALUES
 (1,'a1','2026-09-01', 3200.00,'Employer GmbH','salary'),
 (1,'a2','2026-09-02', -950.00,'Vonovia','rent'),
 (1,'a3','2026-09-05',  -64.30,'REWE','groceries'),
 (1,'a4','2026-09-12',  -12.99,'Netflix','subscriptions'),
 (1,'a5','2026-10-01', 3200.00,'Employer GmbH','salary'),
 (1,'a6','2026-10-02', -950.00,'Vonovia','rent'),
 (1,'a7','2026-10-08',  -81.10,'REWE','groceries'),
 (1,'a7','2026-10-08',  -81.10,'REWE','groceries'),      -- DUPLICATE from re-sync
 (1,'a8','2026-10-15', -230.00,'MediaMarkt',NULL),
 (2,'b1','2026-09-03',  -45.00,'Shell','fuel'),
 (2,'b2','2026-10-03',  -52.00,'Shell','fuel'),
 (3,'c1','2026-09-01', 2800.00,'Uni Köln','salary'),
 (3,'c2','2026-09-20', -400.00,'Landlord Ben','rent'),
 (3,'c3','2026-10-01', 2800.00,'Uni Köln','salary'),
 (3,'c4','2026-10-22', -120.40,'Lidl','groceries'),
 (4,'d1','2026-09-15', -15.00,'Spotify','subscriptions'),
 (4,'d2','2026-10-15', -15.00,'Spotify','subscriptions'),
 (4,'d2','2026-10-15', -15.00,'Spotify','subscriptions'), -- DUPLICATE
 (4,'d3','2026-10-28', 1500.00,'Freelance Client',NULL);
-- account 5 (Dita, Commerzbank) has NO transactions on purpose
