(defun superscript ()

  (format t "Hello, world")

  )
(message "hi")
(message "Her age is: %d" 16)        ; %d is for number
(message "Her name is: %s" "Vicky")  ; %s is for string
(message "Her mid init is: %c" 86)   ; %c is for character in ASCII code
(message "My list is: %S" '(8 2 3))  ; %S is for a list


;; ARICMETIC FUNTIONS

(+ 2 2 2 ) ; returns 6

(setq two 2)     ; it's an integer
(message "%d" two)
(integerp two)   ; returns t

(setq three 3.0) ; it's an decimal number
(message "%d" three)
(integerp three) ; returns nil
(floatp three)   ; returns t

(setq four 4.)   ; it's an integer
(message "%d" four)
(integerp four)  ; returns t

;; CONVERT STRING AND NUMBERS

(string-to-number "5") ; returns 5
(number-to-string 5)   ; returns "5"

;; FUNCTIONS

(defun myFunction ()
  (interactive) ;; make the function available from M-x
  "testing" (message "Yay!")
  )

(defun myFunction (myStart myEnd)
  "Prints region start and end positions"
  (interactive "r")
  (message "Region begin at: %d, end at: %d" myStart myEnd)
  )

(defun myName (yourName)
  "Prints region start and end positions"
  (interactive "s")
  (message "Hello, %s" yourName)
  )
