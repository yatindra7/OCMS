//
// Created by yatindra on 24-03-2022.
//

#ifndef SE_ASS_3_FRACTION_H
#define SE_ASS_3_FRACTION_H

#include <ostream>

template <typename T = int> // T is an integral type like int, char, short, long, etc.
class Fraction_
{         // Implicit assertion for proper fraction: GCD(|n_|, d_) = 1
    T n_; // numerator
    T d_; // denominator
    T GCD(T a, T b)
    {
        if (b == T(0))
            return a;
        return GCD(b, a % b);
    }

public:
    // Constructors and Destructor
    explicit Fraction_(T n = 1, T d = 1);

    Fraction_(const Fraction_<T> &cp);

    virtual ~Fraction_() = default;

    // Gives the arithmetic value of the fraction as a double
    double value(const Fraction_<T> &cp)
    {
        return (double)cp.n_ / (double)cp.d_;
    }

    void REDUCTION()
    {
        if (this->d_ < 0)
        {
            this->d_ = T(-1) * this->d_;
            this->n_ *= T(-1);
        }
        T x = GCD(this->n_, this->d_);
        this->n_ = this->n_ / x;
        this->d_ = this->d_ / x;
    }

    // Comparison operators overload
    bool operator<(const Fraction_<T> &cmpr) const;

    bool operator>(const Fraction_<T> &cmpr) const;

    bool operator<=(const Fraction_<T> &cmpr) const;

    bool operator>=(const Fraction_<T> &cmpr) const;

    bool operator==(const Fraction_<T> &cmpr) const;

    bool operator!=(const Fraction_<T> &cmpr) const;

    Fraction_<T> operator+(const Fraction_<T> &cmpr) const;

    Fraction_<T> operator-(const Fraction_<T> &cmpr) const;

    Fraction_<T> operator*(const Fraction_<T> &cmpr) const;

    Fraction_<T> operator/(const Fraction_<T> &cmpr) const;

    // Fraction_<T> operator%(const Fraction_<T> &cmpr) const;

    // Unary operators
    Fraction_<T> operator!() const;

    Fraction_<T> operator+() const;

    Fraction_<T> operator-() const;

    Fraction_<T> operator++();

    Fraction_<T> operator--();

    friend std::ostream &operator<<(std::ostream &os, const Fraction_<T> &fraction)
    {
        os << fraction.n_ << "/" << fraction.d_;
        return os;
    }
    friend std::istream &operator>>(std::istream &is, Fraction_<T> &fraction)
    {
        std::cout << "[NUM]: ";
        is >> fraction.n_;
        std::cout << "[DEN]: ";
        is >> fraction.d_;
        if (fraction.d_ == 0)
            throw "0 cannot be denominator";
        fraction.REDUCTION();
        return is;
    }
};

template <typename T>
Fraction_<T>::Fraction_(const Fraction_<T> &cp)
{
    this->n_ = cp.n_;
    this->d_ = cp.d_;
    REDUCTION();
}

template <typename T>
Fraction_<T>::Fraction_(T num, T denom) : n_(num), d_(denom)
{
    if (denom == 0)
        throw "[ERROR] DENOMINATOR NULL!!!";
    REDUCTION();
}

template <typename T>
Fraction_<T> Fraction_<T>::operator!() const
{
    return Fraction_<T>(T(this->d_), T(this->n_));
}

template <typename T>
Fraction_<T> Fraction_<T>::operator+() const
{
    return Fraction_<T>(T(this->n_), T(this->d_));
}

template <typename T>
Fraction_<T> Fraction_<T>::operator-() const
{
    return Fraction_<T>(T(-this->n_), T(this->d_));
}

template <typename T>
Fraction_<T> Fraction_<T>::operator++()
{
    this->n_ += this->d_;
    REDUCTION();
    return *this;
}

template <typename T>
Fraction_<T> Fraction_<T>::operator--()
{
    this->n_ -= this->d_;
    REDUCTION();
    return *this;
}

template <typename T>
Fraction_<T> Fraction_<T>::operator+(const Fraction_<T> &cmpr) const
{
    T d = (this->d_ * cmpr.d_);
    T n = this->n_ * cmpr.d_ + cmpr.n_ * this->d_;
    return Fraction_<T>(T(n), T(d));
}

template <typename T>
Fraction_<T> Fraction_<T>::operator-(const Fraction_<T> &cmpr) const
{
    T d = (this->d_ * cmpr.d_);
    T n = this->n_ * cmpr.d_ - cmpr.n_ * d_;
    return Fraction_<T>(n, d);
}

template <typename T>
Fraction_<T> Fraction_<T>::operator*(const Fraction_<T> &cmpr) const
{
    return Fraction_<T>(T(this->n_ * cmpr.n_), T(this->d_ * cmpr.d_));
}

template <typename T>
Fraction_<T> Fraction_<T>::operator/(const Fraction_<T> &cmpr) const
{
    if (cmpr.n_ == T(0))
        throw("[ERROR] DENOMINATOR NULL!!!");
    return Fraction_<T>(T(this->n_ * cmpr.d_), T(this->d_ * cmpr.n_));
}

/*template <typename T>
Fraction_<T> Fraction_<T>::operator%(const Fraction_<T> &cmpr) const
{
    if (cmpr.n_ == T(0))
        throw("[ERROR] NULL FRACTION CAN'T BE USED IN %");
    Fraction_<T> mod;
    mod = *this - Fraction_<T>(T(floor(value(*this / cmpr))), 1) * cmpr;
    return mod;
}*/

template <typename T>
bool Fraction_<T>::operator<(const Fraction_<T> &cmpr) const
{
    // return value(*this) < value(cmpr);
    if (this->n_ * cmpr.n_ < 0)
    {
        if (this->n_ > cmpr.n_)
            return false;
        else
            return true;
    }
    else
    {
        return (this->n_) * (cmpr.d_) < (this->d_) * (cmpr.n_);
    }
}

template <typename T>
bool Fraction_<T>::operator>(const Fraction_<T> &cmpr) const
{
    return cmpr < *this;
}

template <typename T>
bool Fraction_<T>::operator<=(const Fraction_<T> &cmpr) const
{
    return !(cmpr < *this);
}

template <typename T>
bool Fraction_<T>::operator>=(const Fraction_<T> &cmpr) const
{
    return !(*this < cmpr);
}

template <typename T>
bool Fraction_<T>::operator==(const Fraction_<T> &cmpr) const
{
    return n_ == cmpr.n_ && d_ == cmpr.d_;
}

template <typename T>
bool Fraction_<T>::operator!=(const Fraction_<T> &cmpr) const
{
    return !(cmpr == *this);
}

#endif