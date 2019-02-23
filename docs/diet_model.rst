diet - documentation 
---------------------

 - ``Set`` ``F``: 
	Foods. :math:`\mathcal{F}`

	Properties: Dimen=1, Domain=None, Ordered=False, Bounds=None

 - ``Set`` ``N``: 
	Nutrients. :math:`\mathcal{N}`

	Properties: Dimen=1, Domain=None, Ordered=False, Bounds=None

 - ``Param`` ``cost``: 
	Cost of each food. 
        :math:`c_f \geq 0`

	Properties: Index=F, Domain=NonNegativeReals, Default=None, Mutable=False

 - ``Param`` ``content``: 
	Amount of nutrient in each food. 
        :math:`a_{f,n} \geq 0`

	Properties: Index=content_index, Domain=NonNegativeReals, Default=None, Mutable=False

 - ``Param`` ``min_intake``: 
	Lower bound on each nutrient. 
        :math:`y^{min}_n`

	Properties: Index=N, Domain=NonNegativeReals, Default=0.0, Mutable=False

 - ``Param`` ``max_intake``: 
	Upper bound on each nutrient. 
        :math:`y^{max}_n`

	Properties: Index=N, Domain=NonNegativeReals, Default=inf, Mutable=False

 - ``Param`` ``volume``: 
	Volume per serving of food. 
        :math:`v_f`

	Properties: Index=F, Domain=PositiveReals, Default=None, Mutable=False

 - ``Param`` ``max_volume``: 
	Maximum volume of food consumed. 
        :math:`v^{max}`

	Properties: Index=None, Domain=PositiveReals, Default=None, Mutable=False

 - ``Var`` ``x``: 
	Number of servings consumed of each food. 
        :math:`x_f \geq 0`

	Properties: Index=F

 - ``Expression`` ``total_volume``: 
	Total volume of food consumed. 

        .. math:: v^{tot} = \sum_{f \in \mathcal{F}} 
            v_f \cdot x_f

	Properties: Index=None

 - ``Expression`` ``intake``: 
	Total intake of each nutrient. 

        .. math:: y_n = \sum_{f \in \mathcal{F}} 
            \alpha_{f,n} \cdot x_f

	Properties: Index=N

 - ``Objective`` ``minimize_total_cost``: 
	Minimize the cost of food that is consumed. 

        .. math:: \min_{x} \sum_{f \in \mathcal{F}} c_f \cdot x_f

	Properties: Index=None

 - ``Constraint`` ``nutrient_limit``: 
	Enforce upper and lower bounds on intake of each nutrient. 

        .. math:: y^{min}_n \leq y_n \leq y^{max}_n

	Properties: Index=N

 - ``Constraint`` ``volume_limit``: 
	Limit the volume of food consumed. 

        .. math:: v^{tot} \leq v^{max}

	Properties: Index=None
