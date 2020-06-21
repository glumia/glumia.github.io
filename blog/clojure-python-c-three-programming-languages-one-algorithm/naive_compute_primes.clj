;; Clojure implementation of a naive prime numbers calculation algorithm.
;;
;; On my system (a Thinkpad X250 with an Intel i5-5300U CPU)
;; it takes ~12500ms to compute 10000 prime numbers.

(defn next-prime
  "Given a vector of all the prime numbers up to N in ascending order, return the next
  prime number."
  [primes]
  (loop [n (+ 2  (last primes))]
    (if (some zero? (map #(mod n %) primes))
      (recur (+ 2 n))
      n)))

(defn extend-primes
  "Given a vector of all the prime numbers up to N in ascending order extend it
  adding the next prime to the end of the vector."
  [primes]
  (conj primes (next-prime primes)))

(defn primes
  "Get the first N primes."
  [N] ((apply comp (repeat (- N 2) extend-primes)) [2 3]))

