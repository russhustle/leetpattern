select
    v.customer_id,
    count(*) as count_no_trans
from visits as v
left join transactions as t
    on v.visit_id = t.visit_id
where t.transaction_id is null
group by v.customer_id
