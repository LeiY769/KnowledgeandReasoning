<?php
class Database
{
    private static $DB_HOST = 'db';
    private static $DB_USER = 'user';
    private static $DB_PASS = 'root';
    private static $DB_NAME = 'user';

    private static $pdo = null;
    /**
     * Returns PDO object
     * @return PDO|null
     */

    public static function getPDO()
    {
        $dbUsername = self::$DB_USER;
        $dbPassword = self::$DB_PASS;
        $dbHostname = self::$DB_HOST;
        $dbName = self::$DB_NAME;
        
        if (self::$pdo === null) {
            try {
                self::$pdo = new PDO('mysql:dbname=' . $dbName . ';host=' . $dbHostname, $dbUsername, $dbPassword, [
                    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
                    PDO::MYSQL_ATTR_INIT_COMMAND => 'SET NAMES utf8'
                ]);
            } catch (PDOException $e) {
                echo 'Problem : ' . $e->getMessage() . '<br>';
                echo 'Numero : ' . $e->getCode();
                die('Unable todo the do the connection with the databse');
            }
        }
        return self::$pdo;
    }
}