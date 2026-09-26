# Architecture

Django depends on the application and domain layers, never the reverse. The Strategy port makes routing policy replaceable by rules, a model, or a remote service. Validation remains in the domain entity. A production version would add authentication, persistence, structured validation, observability, and a versioned routing policy.
