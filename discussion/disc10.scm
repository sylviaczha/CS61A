"4.1"
(define (factorial x) (if (< x 2) x (* x factorial (- x 1)))

"4.2"
(define (fib n) (if (< n 2) n (+ (fib (- n 1)) (fib (- n 2)))))
 
"5.1"
(define (my-append a b) 
 (cond
  ((eq? a '()) b)
  ((eq? b '()) a)
   (else (cons (car a) (my-append (cdr a) b)))))

"5.2"
(define (find_three s)
 (cond 
  ((eq? s '()) #f)
  ((eq? (car s) list)(find_three (car s)))
  ((eq? (car s) 3) #t)
  (else (find_three (cdr s)))))

"5.3"
 (define (duplicate list)
  (if (eq? lst '()) '()
    (cons (car lst) 
     (cons (car lst)
      (duplicate (cdr lst))))))
  
 "5.4"
 (define (insert element lst index)
  (cond
    ((eq? lst '()) '())
    ((< index 0) '())
    ((> index 0) (insert element (cdr lst) (- index 1)))
    (else (cons element lst))))
