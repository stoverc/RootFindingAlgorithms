(* ::Package:: *)

(* ::Input:: *)
(*ClearAll[Bisection]*)


(*
	This function implements the bisection method.
	Inputs: 
		* a function of the form Function[...];
		* the interval endpoints a and b;
		* the threshold variable eps
	Output:
		* A list of the form {c_end,f[c_end]}
*)
Bisection[f_Function,a_,b_,eps_]:=Module[{
	(* 
		the start interval is fixed.
		since the investigation interal has to change internally, 
		we define new (temp) interval vars "start" and "end"
	*)
	start=a,
	end=b,
	c=(a+b)/2.
},
	(* we want to iteratively whittle away the interval while outside our threshold *)
	While[Abs[f[c]]>=eps,
	(
		(* the "if" condition that defines the bisection method *)
		If[
			f[c]*f[start]<0,
			end=c,
			start=c
		];
		
		(* once we've recomputed "start" and/or "end", we must recompute the midpoint *)
		c=(start+end)/2.;
	)
	];
	
	(* once done, we must be inside our tolerance, so we return the approximate zeros *)
	Return[{c,f[c]}];
]


(* ::Input:: *)
(*Bisection[Function[x,x^3+2x-2],0,1,0.000025]*)


(* ::Input:: *)
(*Bisection[Function[x,x Exp[x]-2],0,1,0.000025]*)


(* ::Input:: *)
(*Bisection[Function[x,Sin[x]],2,4,0.000025]*)
